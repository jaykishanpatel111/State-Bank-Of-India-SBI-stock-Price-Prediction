#!/usr/bin/env python
# coding: utf-8

# ## State Bank Of India (SBI) Stock Price Prediction using Recurrent Neural Network
We have taken State Bank Of India (SBI) stock price dataset. We will take days opening stock price and predict the ouput on that.
# #### Part 1: Data Preprocessing

# In[1]:


# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


cd G:\Done projects\RNN\State Bank Of India (SBI)


# In[3]:


pwd


# In[4]:


# import training set
training_set=pd.read_csv('State Bank Of India (SBI).csv')
training_set


# In[5]:


training_set=training_set.iloc[:,2:3].values


# In[6]:


training_set

# MinMaxScaler transform the dataset into the range of (0,1). Here is formula below
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# X_scaled = X_std * (max - min) + min
# In[7]:


# feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc= MinMaxScaler()
training_set=sc.fit_transform(training_set)


# In[8]:


training_set


# In[9]:


# Getting the input and output
X_train= training_set[0:1257]
y_train= training_set[1:1258]


# In[10]:


X_train


# In[11]:


y_train


# In[12]:


# Reshaping
X_train=np.reshape(X_train, (1257 , 1 , 1))


# #### Part 2: Building the RNN

# In[13]:


# importing the Keras libraries and Packages
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM


# In[14]:


# initialize the RNN 
model = Sequential()


# In[15]:


# adding the input layer and LSTM layer
model.add(LSTM(units=256, activation= 'sigmoid', input_shape= (None,1)))


# In[16]:


# adding the output layer
model.add(Dense( units=1 ))   # units= Number of outputs  


# In[17]:


# compiling the RNN
model.compile(optimizer='adam', loss='mean_squared_error')


# In[18]:


# fitting the RNN to the training set
model.fit(X_train, y_train, batch_size=128, epochs=200)


# #### Part 3: Making the Prediction and Visulising the result

# In[19]:


# Geting the real stock price of 2017
test_set = pd.read_csv('State Bank Of India_test.csv')
real_stock_price = test_set.iloc[:,2:3].values


# In[20]:


real_stock_price


# In[21]:


# Geting the Predicted Stock Price of 2017
inputs = real_stock_price


# In[22]:


inputs = sc.transform(inputs)


# In[23]:


inputs = np.reshape(inputs, (real_stock_price.size , 1, 1))


# In[24]:


predicted_stock_price = model.predict(inputs)


# In[25]:


predicted_stock_price = sc.inverse_transform(predicted_stock_price)


# In[26]:


predicted_stock_price


# In[27]:


# Visulising the Result 
plt.plot( real_stock_price , color = 'red' , label = 'Real Stock Price')
plt.plot( predicted_stock_price , color = 'blue' , label = 'Predicted Stock Price')
plt.title('SBI Price Prediction')
plt.xlabel( 'Time' )
plt.ylabel( 'SBI Price' )
plt.legend()
plt.show()


# In[28]:


from sklearn.metrics import r2_score, mean_squared_error


# In[29]:


r2_score(real_stock_price,predicted_stock_price)


# In[30]:


np.sqrt(mean_squared_error(real_stock_price,predicted_stock_price))


# # 9. Save Weights & Loading the model

# In[33]:


model.save('SBI.h5')


# In[34]:


model.load_weights('SBI.h5')


# In[ ]:





# In[ ]:




