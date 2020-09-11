from keras.models import load_model

model = load_model('./cifar.h5')

print(model.get_weights())
