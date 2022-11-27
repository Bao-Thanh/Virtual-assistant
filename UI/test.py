import pickle
def word(password):
    character=[]
    for i in password:
        character.append(i)
    return character

password ='abc'
model = pickle.load(open('models/RandomForestClassifier.pkl', 'rb'))
tf = pickle.load(open('models/tdif.pkl', 'rb'))
test = tf.transform([password]).toarray()
output = model.predict(test)
result = str(password + ' có độ bảo mật ' + output)
print(result)