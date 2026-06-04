{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "886a6eb6-5923-4de2-b47c-77f471b2cd14",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2068402a-cb26-4018-b1a9-d2de8242a4dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1f4b9904-0ff9-422f-927d-ea21ce79be69",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"laboratory__data.csv\")\n",
    "df.columns = df.columns.str.strip()\n",
    "\n",
    "x = df[[\"Glucose\", \"Hemoglobin\", \"Cholestrol\"]]\n",
    "y = df[\"Disease\"]\n",
    "x_train, x_test, y_train, y_test = train_test_split(\n",
    "    x,\n",
    "    y,\n",
    "    test_size=0.2,\n",
    "    random_state=42\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "020ba7ce-1e55-474b-a3ce-d4d0d2180b9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "saved\n"
     ]
    }
   ],
   "source": [
    "model = RandomForestClassifier(\n",
    "    n_estimators=100,\n",
    "    random_state=42\n",
    ")\n",
    "model.fit(x_train, y_train)\n",
    "with open(\"healthmodel.pkl\", \"wb\") as f:\n",
    "    pickle.dump(model, f)\n",
    "\n",
    "print(\"saved\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48493a65-b632-4d79-91ee-511f85d5f37f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
