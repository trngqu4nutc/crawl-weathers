<template>
  <div>
    <h1>Dự đoán {{ number }} ngày tiếp theo</h1>
    <hr />
    <div class="row row-cols-1 row-cols-md-4 row-cols-lg-4">
      <!-- <transition name="slide"> -->
        <Day v-for="(weather, i) in weathers" v-bind:key="i" v-bind:weather="weather" />
      <!-- </transition> -->
    </div>
  </div>
</template>

<script>
import Day from "./card/Day";
import axios from "axios";
export default {
  data() {
    return {
      number: parseInt(this.$route.query.number),
      weathers: []
    };
  },
  components: {
    Day
  },
  watch: {
    $route(to, from) {
      this.number = parseInt(to.query.number);
      axios.get('http://localhost:4000/days', {
        params: {
          number: this.number
        }
      })
      .then(res => {
        this.weathers = res.data;
      })
      .catch(err => console.log(err));
    }
  },
  created(){
    axios.get('http://localhost:4000/days', {
        params: {
          number: this.$route.query.number
        }
      })
      .then(res => {
        this.weathers = res.data;
      })
      .catch(err => console.log(err));
  }
};
</script>

<style>
</style>