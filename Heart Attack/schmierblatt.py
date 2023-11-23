# Erstellen und Trainieren des logistischen Regressionsmodells
model = LogisticRegression()
model.fit(X_train, y_train)

# Vorhersagen auf Testdaten
y_pred = model.predict(X_test)

# Bewertung des Modells
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Genauigkeit:", accuracy)
print("Konfusionsmatrix:\n", conf_matrix)
print("Klassifikationsbericht:\n", class_report)