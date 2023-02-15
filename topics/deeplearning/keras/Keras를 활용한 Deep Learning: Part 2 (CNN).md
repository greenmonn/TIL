# Keras를 활용한 Deep Learning: Part 2 (CNN)
## CNN (Convolutional Neural Network)
- 특정 구조의 Layer를 사용하는 Neural Network
- 2차원/3차원 공간 구조로 이루어진 데이터를 학습시키는 데에 적합하다.
- 이미지 Classification에 유용하다.

## DNN for image classification
- input data가 이미지를 이루는 모든 바이트. (한 바이트가 하나의 색상 정보를 갖고 있다)
- 이미지의 ‘형상’은 고려하지 않고, 단순히 raw data를 직접 처리하기 때문에 네트워크에 필요한 weight와 bias 갯수가 지나치게 많아진다.

## Convolutional Layer
- Filter를 사용하여 입력 이미지를 처리하는 레이어
- Filter는 Weight를 Grid 형태로 모은 구조
- 각 Filter의 weight는 random하게 초기화되어 있으며, image를 가로지르며 계산하게 된다. 
- **N개의 Filter를 사용하여 이미지의 특징(패턴)을 학습한다.**: 각각의 고유한 패턴을 이미지가 포함하는지, 아닌지를 판단할 수 있다.

- In `Keras`:
```python
model.add(Conv2D(filters=16, kernel_size=(5,5), activation='relu', input_shape=(28,28,1)) # 3 if RGB
```
`Dense` 레이어 대신 Convolutional Layer를 추가한다.
이 경우 Weight Filter는 5*5 pixels의 16개로 이루어져 있다.

## Stride & Padding
### Strides
- default: 1
- Filter가 이미지를 가로지르는 ‘보폭’의 개념

### Padding
- default: ‘valid’
- Filter가 이미지 경계를 넘어갔을 때 처리 방식
- “Valid”: Filter에 매칭되지 않는 부분의 계산을 drop
- “Same”: Filter에 매칭되지 않는 부분을 0으로 채워넣어서 계산

## Pooling Layer
- 입력을 Down-sampling하기 위한 목적
- Output을 down-scale한다.
- In `Keras`:
```
model.add(MaxPool2D(pool_size=(2,2))
```

- Image의 크기를 감소하고, Filter의 차원을 증가시킬 수 있다.

## Pre-trained Model
### IMAGENET
- http://image-net.org/

- ImageNet challenge를 거쳐서 검증을 완료한 이미지 classification 모델
- pre-trained model을 재사용하여 개발 시간을 단축할 수 있다.

### Fine Tuning / Transfer Learning
- 새로운 데이터에 pre-trained 모델을 재사용하는 것.
- 재사용/재학습의 범위를 자유롭게 조정해서 사용할 수 있다.
- 새로운 데이터의 size와 pre-trained 데이터와의 유사성을 확인해서 재사용할 부분과 재학습할 부분을 구분할 수 있다.


## 실습
- Flattening Step: [Convolutional Neural Networks (CNN): Step 3 - Flattening](https://www.superdatascience.com/convolutional-neural-networks-cnn-step-3-flattening/)

- Pre-trained Model 재사용
	1. Layer를 not-trainable하게 만드는 방법
	2. Bottleneck Feature를 사용하는 방법
		- [using pre trained VGG16 for another classification task](https://github.com/keras-team/keras/issues/4465)


