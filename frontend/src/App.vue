<template>
  <div>
    <nav class="navbar">
      <h1>&nbsp;Restaurant Data based on Postcode</h1>
      <div class="navbar-logo">
        <img src="img/justeat.png" alt="Just Eat Logo">
      </div>
    </nav>
    <div class="search-container">
      <input v-model="postcode" placeholder="Enter postcode to view first 10 restaurants in the area" class="search-input"/>
      <button @click="fetchRestaurants" class="search-button">Search</button><br>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    </div>
    <div class="restaurants-container">
      <div v-for="restaurant in restaurants" :key="restaurant.Name" class="restaurant-item">
        <h3>{{ restaurant.Name }}</h3>
        <p><b>Cuisines: </b>{{ restaurant.Cuisines }}</p>
        <p><b>Rating: </b>{{ restaurant.Rating }}</p>
        <p><b>Address: </b>{{ restaurant.Address.firstLine }}, {{ restaurant.Address.city }}, {{ restaurant.Address.postalCode }}</p>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      postcode: '',
      restaurants: [],
      errorMessage: ''
    };
  },
  methods: {
    fetchRestaurants() {
      this.errorMessage = ''; 
      const url = `http://localhost:8000/api/restaurants/${this.postcode}/`;
      fetch(url, {method: 'GET'})
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          if (data.error) {
            this.errorMessage = data.error;
          } else {
            this.restaurants = data;
          }
        })
        .catch(error => {
          console.error('There was a problem with the fetch operation:', error);
          this.errorMessage = error.message;
        });
    }
  }
};
</script>

<style>

.navbar h1 {
  color: white;
  padding: 0; 
  
}
.navbar {
  background-color: #ed641f;
  padding: 10px;
  text-align: center;
}

.navbar-logo img {
  height: auto; 
  max-width: 20em;
  max-height: 20em;
}
.search-container {
  display: flex;
  justify-content: center;
  padding: 20px;
  gap: 10px;
}

.search-input {
  width: 420px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.search-button {
  padding: 10px 15px;
  background-color: #ed641f;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #d37811;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}

.restaurants-container {
  padding: 20px;
}

.restaurant-item {
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 10px;
}
</style>

