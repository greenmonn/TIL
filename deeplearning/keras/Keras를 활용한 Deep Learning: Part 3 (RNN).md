# Keras를 활용한 Deep Learning: Part 3 (RNN)
## RNN(Recurrent Neural Network)
![](Keras%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%92%E1%85%AA%E1%86%AF%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20Deep%20Learning:%20Part%203%20(RNN)/screenshot%202019-01-10%20PM%2011.43.53.png)

- 첫 번째 Input이 두 번째 Input에 영향을 주는 형태
- Input을 입력하는 순서가 결과에 영향을 준다.
- ex) 날씨 데이터, 교통량 등 축적된 데이터


## RNN의 학습 유형
	- Many to One
	- Many to Many
	- One to Many
	- One to One

## Gradient Vanishing
	- Time Step을 200~300 이상으로 설정할 때 gradient vanishing 문제가 발생할 수 있다.

## LSTM, GRU Layer
### LSTM (Long Term Shot Memory)
	- Gradient vanishing 문제를 해결할 수 있도록 RNN cell을 변경한 구조
```python
model = Sequential()
model.add(LSTM(256, input_shape=(10, 1)))
model.add(LSTM(256))
```

###  GRU (Gated Recurrent Unit)
```python
model = Sequential()
model.add(GRU(256, input=shape(10, 1)))
model.add(GRU(256))
```

### Input/Output
- Input은 (N Sample, N time step, Value)의 형태로 주어진다.
- Many to One: Output은 단순한 value 형태
	- (N Sample, Value)
	- ` return_sequences=False`
- Many to Many: Output은 Time Step을 고려한 3차원 데이터
	- (N Sample, N time step, Value)
	-  ` return_sequences=True`


### 참고 링크 추가
- 헷갈리는 Batch/Epoch 개념: [Epoch vs Batch Size vs Iterations – Towards Data Science](https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9)










