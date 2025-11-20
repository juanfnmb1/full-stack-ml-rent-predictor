<template>
  <div class="rent-predictor">
    <div id= "icon"><i class="fa-solid fa-house"></i> </div>
    <h1>Rent Predictor</h1> 
     
    <p class="subtitle">Enter property details to estimate its monthly rent!</p>

    <form @submit.prevent="getPrediction">
      <div class="form-group">
        <label for="bedrooms">Bedrooms</label>
        <input 
          type="number" 
          id="bedrooms" 
          v-model.number="formData.bedrooms" 
          min="1" 
          max="6" 
          required
        >
      </div>

      <div class="form-group">
        <label for="bathrooms">Bathrooms</label>
        <input 
          type="number" 
          id="bathrooms" 
          v-model.number="formData.bathrooms" 
          min="1" 
          max="6" 
          step="0.5"
          required
        >
      </div>

      <div class="form-group">
        <label for="sqft">Square Feet</label>
        <input 
          type="number" 
          id="sqft" 
          v-model.number="formData.sqft" 
          min="100" 
          max="10000" 
          required
        >
      </div>

      <div class="form-group">
        <label for="location">Location</label>
        <select id="location" v-model="formData.location" required>
          <option value="downtown">Downtown</option>
          <option value="suburb">Suburb</option>
        </select>
      </div>

      <div class="form-group">
        <label for="property_type">Property Type</label>
        <select id="property_type" v-model="formData.property_type" required>
          <option value="apartment">Apartment</option>
          <option value="townhouse">Townhouse</option>
          <option value="house">House</option>
        </select>
      </div>

      <button type="submit" :disabled="loading">
        {{ loading ? 'Calculating...' : 'Predict Rent' }}
      </button>
    </form>

    <div v-if="prediction !== null" class="prediction-result">
      <h2>Estimated Monthly Rent</h2>
      <div class="rent-amount">${{ prediction.toLocaleString() }}</div>

      <p class="result-info" v-if="submittedData">
        Based on a {{ submittedData.bedrooms }} bed,
        {{ submittedData.bathrooms }} bath,
        {{ submittedData.sqft }} sqft,
        {{ submittedData.property_type }} in {{ submittedData.location }}.
      </p>
    </div>

    <div v-if="error" class="error-message">
      {{ error }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RentPredictor',
  data() {
    return {
      formData: {
        bedrooms: 2,
        bathrooms: 1,
        sqft: 850,
        property_type: 'apartment',
        location: 'downtown'
      },
      prediction: null,
      submittedData: null,  // <-- holds frozen values
      loading: false,
      error: null
    }
  },
  methods: {
    async getPrediction() {
      this.loading = true
      this.error = null

      try {
        const backendUrl = `${window.location.protocol}//${window.location.hostname}:8000/predict`
        const response = await axios.post(backendUrl, this.formData)

        if (response.data.success) {
          this.prediction = response.data.predicted_rent
          this.submittedData = { ...this.formData } // <-- freeze the values
        } else {
          this.error = 'Failed to get prediction'
        }
      } catch (err) {
        this.error = 'Error connecting to server. Please make sure the backend is running.'
        console.error('Prediction error:', err)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.rent-predictor {
  background: white;
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

h1 {
  color: #667eea;
  font-size: 2.5rem;
  margin-bottom: 10px;
  text-align: center;
}

.subtitle {
  color: #666;
  text-align: center;
  margin-bottom: 30px;
  font-size: 1.1rem;
}

form {
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: #333;
  font-weight: 600;
  font-size: 0.95rem;
}

input, select {
  width: 100%;
  padding: 12px 15px;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

input:focus, select:focus {
  outline: none;
  border-color: #667eea;
}

button {
  width: 100%;
  padding: 15px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.prediction-result {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 30px;
  border-radius: 15px;
  text-align: center;
  color: white;
  margin-top: 30px;
}

.prediction-result h2 {
  font-size: 1.3rem;
  margin-bottom: 15px;
  color: white;
}

.rent-amount {
  font-size: 3rem;
  font-weight: bold;
  margin: 20px 0;
}

.result-info {
  font-size: 0.95rem;
  opacity: 0.9;
}

.error-message {
  background: #fee;
  color: #c33;
  padding: 15px;
  border-radius: 10px;
  margin-top: 20px;
  text-align: center;
}
#icon{
  color: #667eea;
  font-size: 2rem;
  text-align: center;
  margin-bottom: -20px;
  }
</style>
