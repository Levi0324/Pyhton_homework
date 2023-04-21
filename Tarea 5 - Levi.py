#Tarea 5 Funciones 

from sklearn.model_selection import train_test_split
X = df.drop('status', axis = 1)
y = df['status']

X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                   stratify = y,
                                                    test_size = 0.3,
                                                   random_state = 101)

n_random = 7

RF = RandomForestClassifier(n_random)
RF.fit(X_train, y_train)
print('Accuracy of RF classifier on training set: {:.2f}'
     .format(RF.score(X_train, y_train)))
print('Accuracy of RF classifier on test set: {:.2f}'
     .format(RF.score(X_test, y_test)))

RF =  RandomForestClassifier()
RF.fit(X_train,y_train)
predRF = RF.predict(X_test)
cf_matrixRF = confusion_matrix(y_test, predRF)
sns.heatmap(cf_matrixRF/np.sum(cf_matrixRF), annot=True, 
            fmt='.2%', cmap='Reds')
plt.title('Matriz de confusión de  RandomForest', fontweight='bold', fontsize=16)
plt.xlabel('Predicción', fontweight='bold', fontsize=12)
plt.ylabel('Real', fontweight='bold', fontsize=12)

cf_matrixRF
