<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>Random number from backend: {{ randomNumber }} served by {{ container }}</p>
    <button @click="getRandom">New random number</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  data() {
    return {
      randomNumber: 0,
      container: 'null'
    };
  },
  methods: {
    getRandomInt(min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min + 1)) + min;
    },
    getRandom() {
      // this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend();
    },
    getRandomFromBackend() {
      const path = window.location.origin+':5001/api/random';
      axios
        .get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber;
          this.container = response.data.host
        })
        .catch(error => {
          console.log(error); 
        });
    }
  },
  created() {
    this.getRandom();
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
