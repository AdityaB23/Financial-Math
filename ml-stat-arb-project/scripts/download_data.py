{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1da1262a-2dbb-4a26-82f1-3f6191c28e01",
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "TICKERS = [\"SPY\",\"QQQ\",\"IWM\",\"TLT\",\"IEF\",\"SHY\",\"GLD\"]\n",
    "\n",
    "data = yf.download(\n",
    "    TICKERS,\n",
    "    start=\"2010-01-01\",\n",
    "    auto_adjust=True,\n",
    "    progress=False\n",
    ")\n",
    "\n",
    "prices = data[\"Close\"]\n",
    "prices.to_csv(\"data/processed/prices.csv\")\n",
    "\n",
    "print(\"Data downloaded and cached.\")"
   ]
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
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
