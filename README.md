# Timbre

A scalable system that deploys multiple regression models and time series analysis to predict future stream counts for tracks on the Audius platform, leveraging AWS and Kubernetes.

## Overview

This project predicts stream counts over various timeframes (daily, weekly, monthly, yearly) using data fetched from the Audius API and processed with multiple machine learning models. FastAPI serves as the interface for predictions, and the infrastructure is deployed using AWS EKS for scalability.

## Features

- Predict stream counts for different timeframes (daily, weekly, monthly, yearly).
- Multiple regression models &/or time-series analysis to handle various time horizons.
- FastAPI for API interactions.
- Scalable and efficient deployment using AWS EKS.

## System Architecture

- **Audius API**: Fetches historical streaming data.
- **ML Models**: Regression models trained on historical data for stream prediction.
- **FastAPI**: REST API to serve predictions based on user input.
- **AWS EKS**: Kubernetes cluster ensures scalable model deployment.
  
## Future Ideas

- Smart contract integration for decentralized predictions.
- Incorporate external data sources (e.g., social media trends) for enhanced accuracy.
- Extend models to predict long-term streams (up to 5 years).

## Development Roadmap

- **Phase 1**: Build and deploy the basic prediction model.
- **Phase 2**: Optimize models for different timeframes.
- **Phase 3**: Integrate with Audius smart contracts for decentralized functionality.

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/audius-stream-prediction.git
   cd audius-stream-prediction
