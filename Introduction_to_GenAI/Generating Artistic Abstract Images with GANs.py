import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
import matplotlib.pyplot as plt
from tqdm import tqdm

# Part 1: Dataset Preparation

def load_and_preprocess_images(dataset_path, img_size=(128, 128)):
    """
    Loads and preprocesses images from the dataset directory.
    - Resizes images to a fixed dimension.
    - Normalizes pixel values between 0 and 1.
    - Converts images into NumPy arrays for GAN training.
    """
    image_data = []
    image_files = [f for f in os.listdir(dataset_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    for img_file in tqdm(image_files, desc="Processing images"):
        img_path = os.path.join(dataset_path, img_file)
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=img_size)
        img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0  # Normalize to [0, 1]
        image_data.append(img_array)
    
    return np.array(image_data)

# Example usage
dataset_path = "C:/Users/user/Downloads/pg75679-images.html"
processed_images = load_and_preprocess_images(dataset_path)

# Display sample images
plt.figure(figsize=(10, 5))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(processed_images[i])
    plt.axis('off')
plt.show()

# Save preprocessed data for GAN training
np.save("abstract_art_preprocessed.npy", processed_images)

# Part 2: Building the GAN

# Generator Model
def build_generator(latent_dim):
    model = models.Sequential([
        layers.Dense(128 * 32 * 32, activation="relu", input_dim=latent_dim),
        layers.Reshape((32, 32, 128)),
        layers.Conv2DTranspose(128, (4,4), strides=(2,2), padding='same', activation='relu'),
        layers.Conv2DTranspose(64, (4,4), strides=(2,2), padding='same', activation='relu'),
        layers.Conv2DTranspose(3, (4,4), strides=(1,1), padding='same', activation='sigmoid')
    ])
    return model

# Discriminator Model
def build_discriminator(img_shape):
    model = models.Sequential([
        layers.Conv2D(64, (4,4), strides=(2,2), padding='same', input_shape=img_shape),
        layers.LeakyReLU(alpha=0.2),
        layers.Conv2D(128, (4,4), strides=(2,2), padding='same'),
        layers.LeakyReLU(alpha=0.2),
        layers.Flatten(),
        layers.Dense(1, activation='sigmoid')
    ])
    return model

# Define latent space and input shape
latent_dim = 100
img_shape = (128, 128, 3)

# Initialize generator and discriminator
generator = build_generator(latent_dim)
discriminator = build_discriminator(img_shape)
discriminator.compile(loss='binary_crossentropy', optimizer=optimizers.Adam(learning_rate=0.0002), metrics=['accuracy'])

# GAN Model (Adversarial Training)

def build_gan(generator, discriminator):
    discriminator.trainable = False  # Ensure generator trains while discriminator is fixed
    model = models.Sequential([generator, discriminator])
    model.compile(loss='binary_crossentropy', optimizer=optimizers.Adam(learning_rate=0.0002))
    return model

gan = build_gan(generator, discriminator)

# Training Function
def train_gan(dataset, epochs=10000, batch_size=64):
    real_labels = np.ones((batch_size, 1))
    fake_labels = np.zeros((batch_size, 1))
    
    g_losses, d_losses = [], []  # Store losses for visualization
    
    for epoch in range(epochs):
        # Train Discriminator
        idx = np.random.randint(0, dataset.shape[0], batch_size)
        real_images = dataset[idx]
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        fake_images = generator.predict(noise)
        
        d_loss_real = discriminator.train_on_batch(real_images, real_labels)
        d_loss_fake = discriminator.train_on_batch(fake_images, fake_labels)
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
        
        # Train Generator
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        g_loss = gan.train_on_batch(noise, real_labels)
        
        g_losses.append(g_loss)
        d_losses.append(d_loss[0])
        
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}: D Loss = {d_loss[0]:.4f}, G Loss = {g_loss:.4f}")
            generate_and_save_images(epoch, generator, latent_dim)
    
    # Plot training loss curves
    plt.plot(g_losses, label="Generator Loss")
    plt.plot(d_losses, label="Discriminator Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.title("Training Loss Curves")
    plt.show()

# Part 3: Generating and Evaluating Images

def generate_and_save_images(epoch, generator, latent_dim, num_images=5):
    """
    Generates and saves abstract art images using the trained generator.
    """
    noise = np.random.normal(0, 1, (num_images, latent_dim))
    generated_images = generator.predict(noise)
    
    plt.figure(figsize=(10, 5))
    for i in range(num_images):
        plt.subplot(1, num_images, i+1)
        plt.imshow(generated_images[i])
        plt.axis('off')
    plt.savefig(f"gan_generated_epoch_{epoch}.png")
    plt.show()

# Generate new abstract art images
def evaluate_generated_images(generator, latent_dim, num_images=10):
    """
    Evaluates and visualizes generated abstract art.
    """
    print("Generating and Evaluating Abstract Art Images...")
    generate_and_save_images("final", generator, latent_dim, num_images)
    
    # Subjective evaluation questions
    print("Evaluation Questions:")
    print("- Are the images visually appealing?")
    print("- Do they resemble abstract art in the dataset?")
    print("- How diverse are the generated images?")

# Load preprocessed dataset
dataset = np.load("abstract_art_preprocessed.npy")

# Train GAN
train_gan(dataset)

# Evaluate the final generator output
evaluate_generated_images(generator, latent_dim)
