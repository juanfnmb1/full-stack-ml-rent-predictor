# Rent Predictor Application

## Overview
A full-stack rent prediction application using multivariate linear regression. The backend is built with Python Flask and scikit-learn, while the frontend uses Vue.js.

## Project Architecture
- **Backend**: Python Flask REST API (port 8000)
  - Multivariate linear regression model
  - Trained on dummy data (bedrooms, bathrooms, sqft, location)
  - Provides `/predict` endpoint for rent predictions
  
- **Frontend**: Vue.js SPA (port 5000)
  - Input form for property features
  - Real-time prediction display
  - Clean, responsive design

## Recent Changes
- Initial project setup (November 14, 2025)
- Python backend with Flask and scikit-learn
- Vue.js frontend with prediction form

## Stack
- Backend: Python 3.11, Flask, scikit-learn, numpy, pandas
- Frontend: Node.js 20, Vue 3, Axios
