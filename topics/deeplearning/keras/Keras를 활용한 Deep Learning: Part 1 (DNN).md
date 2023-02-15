# Keras를 활용한 Deep Learning: Part 1 (DNN)

## Perceptron: 하나의 인공 신경 구조
![](Keras%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20Deep%20Learning:%20Part%201%20(DNN)/screenshot%202019-01-06%20AM%2010.24.27.png)
	- Input -> Hidden -> Output
	- Hidden layer는 두 개의 function으로 구성
		- Linear Function
		- Activation Function
	- Feed Forward: 주어진 input x에서 뉴럴넷을 거쳐 y를 계산하는 과정. (cycle을 형성하지 않는다)
	- Activation Function: non-linearity
		- 현실의 데이터는 n차원의 비선형 분포로 존재하기 때문에, Activation Function은 Neural Network에서 비선형 분포를 반영할 수 있도록 하는 역할을 한다.
		- ReLU: 현재 가장 좋은 결과를 보여준다.


> Regression vs. Classification  
>   
> - Regression은 수치 보간 (확률적 추정)  
> - Classification은 ‘어떤 그룹’에 속했는지를 판별 (분류)   

- Error Function (=Cost Function, Loss Function)
	- Neural Net 모델이 Feed Forward로 계산한 값과 실제 타겟 값을 비교하는 데 사용되는 함수
	- MSE, categorical cross-entropy
- Optimizer
	- Neural Net에서 Linear function의 w, b 값을 어떻게 업데이트할지에 대해(어떻게 에러를 줄일 것인지) 사용되는 알고리즘
	- 아래의 경우에는 기울기에 일정 상수(learning rate)를 곱해서 (Gradient descent)
![](Keras%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20Deep%20Learning:%20Part%201%20(DNN)/screenshot%202019-01-06%20PM%202.30.11.png)

- Back Propagation
	- Feed forward의 반대 개념
	- y의 값을 보고 w와 b의 값을 업데이트한다.

## Deep Neural Net
	- Perceptron과는 달리 여러 개의 노드가 함께 연결되어 있다.
	- 기본적으로 Feed Forward -> Back Propagation으로 이뤄지는 과정은 Perceptron과 같다.
	- Training은 모든 Input에 대해서 Feed Forward와 Back Propagation을 수행하는 것.
![](Keras%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20Deep%20Learning:%20Part%201%20(DNN)/screenshot%202019-01-06%20PM%202.38.46.png)


> Neural Network에 대한 괜찮은 설명  
> [But what *is* a Neural Network? - YouTube](https://www.youtube.com/watch?v=aircAruvnKk)  
> Neuron is a function.  
> Deep Neural Network는 여러 개의 뉴런으로 이루어진 Matrix 연산을 다룬다.  
> Training 과정은 적절한 weight와 bias 값을 찾는 과정.  


## Classification with Deep Learning
- Classification의 경우에 X(Input), Y(Target)을 어떻게 표현할 것인가?

### Binary Classification Output

![](Keras%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20Deep%20Learning:%20Part%201%20(DNN)/screenshot%202019-01-07%20PM%204.32.31.png)
- 입력이 어떤 Class{Red, Blue}에 속할지에 대한 확률.
- 0 - 1까지의 값을 가진다.

### Neural Net Input = Features
- Input에서 하나의 특징 = Feature
- 입력은 Feature의 N Size Array
- Linear Function은 다항일차함수

### Feed Forward
- 기준선에 대한 거리를 확률 분포로 나타내기
	- Sigmoid Function(어떤 입력을 받아도 0-1 사이에서 값을 얻을 수 있다)을 Activation Function으로 사용한다.
![](Keras%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20Deep%20Learning:%20Part%201%20(DNN)/screenshot%202019-01-07%20PM%204.56.19.png)

### Error Function
- Classification에서는 MSE 대신 Cross-entropy를 사용한다.
- Cross-entropy
	- 확률 분포 간의 차이를 구하는 함수(각 확률에 음수 자연로그(`-ln`)을 취해서 더해준다)
	- `ln(1) = 0` 임을 이용해서 1과 가까울수록 더 낮은 Error 값이 나온다.
	- 전체 입력 확률을 종합하여 Error를 계산한다.
	- Binary Cross Entropy, Categorical Cross Entropy(Multi-class)

- Back Propagation
	- Cross Entropy를 낮추는 것이 목표
	- Gradient Descent: Regression과 동일하게 에러의 최저점을 찾는다(기울기 미분)
	
### Multi Class Classification
- One-hot Encoding
	- N개의 Class를 가진 데이터의 Y Target 값을 설정할 때
	- N개의 배열로 나타낸다.
- Softmax Function
	- Activation Function으로 나온 값을 확률 분포로 변환


## 실습
[UCI Machine Learning Repository: Adult Data Set](http://archive.ics.uci.edu/ml/datasets/Adult)
인구 조사 데이터를 통해 소득 수준 판별

### Overfitting
![](Keras%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20Deep%20Learning:%20Part%201%20(DNN)/screenshot%202019-01-08%20PM%201.01.21.png)

Accuracy는 증가하지만 Validation Accuracy는 감소하는 경우.
현재 ‘학습하고 있는’ 데이터들에 대한 정확도는 꾸준히 증가하지만, 그 외의 데이터들에 대해서는 정확도가 점점 떨어진다.

- Keras Dense Layer에 대한 유용한 설명(레고 비유): [다층 퍼셉트론 레이어 이야기](https://tykimos.github.io/2017/01/27/MLP_Layer_Talk/)

## Hyper Parameters
### Learning Rate
- Optimizer에 대한 변수.
- 일반적으로 default로 적용되는 값이다.
- Learning Rate를 높일수록 더 빠르게 학습이 진행 (너무 높은 경우에는 optimal point를 지나쳐버릴 수 있음

### Over Fitting
- Validation Data의 Error를 확인하는데, 현재 ‘보고 있는 데이터’에 대한 정확도는 높아지지만 보고 있지 않은 데이터에 대해서는 정확도가 점점 떨어지는 경우. 
- Over Fitting을 방지: Dropout
```python
model = Sequential()
model.add(Dense(32))
model.add(DropOut(0.5)) # 전달된 output의 일부를 사용하지 않는다
model.add(Dense(16))
..
```


## Online Learning & Batch Learning
```
model.fit(X_train, Y-train, epochs=100, batch_size = 100)
```

- Online learning은 한 epoch에서 단 한 번만 weight를 업데이트한다. 
	- 메모리 많이 소모
- Batch learning은 한 epoch에서 batch size만큼 error가 누적되면 그때 업데이트한다.
	- 조금 느리지만 메모리 덜 소모
	- 기본적으로 keras는 batch size = 32로 설정되어 있다.’


- 좀더 전반적으로 딥러닝 전체를 아우른 설명: [기계학습 / 딥러닝이란 무엇인가](https://www.slideshare.net/yonghakim900/ss-60252533)