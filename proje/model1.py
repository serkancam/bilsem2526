import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# 1. VERİLERİ HAZIRLAMA
# 'verisetinin_klasor_yolu' yazan yere klasörünün gerçek yolunu yazmayı unutma!
veriyolu = '/home/ogrenci2/Belgeler/ahmetfurkan_2526/archive/Data' 

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_data = datagen.flow_from_directory(
    veriyolu,
    target_size=(48, 48),
    batch_size=32,
    color_mode='grayscale',
    class_mode='categorical',
    subset='training'
)

test_data = datagen.flow_from_directory(
    veriyolu,
    target_size=(48, 48),
    batch_size=32,
    color_mode='grayscale',
    class_mode='categorical',
    subset='validation'
)

# 2. MODELİ OLUŞTURMA
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(5, activation='softmax') 
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# --- ASIL ÖNEMLİ KISIM BURASI ---
# Modeli gerçekten eğiten komut budur. Bu olmazsa grafik çizilemez.
print("Eğitim başlıyor...")
history = model.fit(train_data, epochs=10, validation_data=test_data)

# 3. BAŞARI GRAFİĞİNİ ÇİZDİRME
plt.figure(figsize=(10, 5))
plt.plot(history.history['accuracy'], label='Eğitim Başarısı')
plt.plot(history.history['val_accuracy'], label='Test Başarısı')
plt.title('Model Başarı Tablosu')
plt.xlabel('Tur (Epoch)')
plt.ylabel('Başarı Oranı')
plt.legend()
plt.show()