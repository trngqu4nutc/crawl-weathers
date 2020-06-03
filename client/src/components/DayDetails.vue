<template>
  <div class="card-deck">
    <CardWeather v-for="(data, i) in datas" v-bind:key="i" v-bind:data="data"></CardWeather>
  </div>
</template>

<script>
import CardWeather from "./card/CardWeather";
import axios from "axios";
export default {
  props: ['date'],
  data() {
    return {
      datas: []
    };
  },
  components: {
    CardWeather
  },
  created() {
    if (this.$route.query.seach) {
      axios
        .get("http://localhost:4000/weather", {
          params: {
            seach: this.date
          }
        })
        .then(res => {
          this.datas = res.data;
        })
        .catch(err => console.log(err));
    } else {
      axios
        .get("http://localhost:4000/weather")
        .then(res => {
          this.datas = res.data;
        })
        .catch(err => console.log(err));
    }
  },
  watch: {
    $route(to, from) {
      if(this.date != ''){
        axios
          .get("http://localhost:4000/weather", {
            params: {
              seach: this.date
            }
          })
          .then(res => {
            this.datas = res.data;
          })
          .catch(err => console.log(err));
      }else{
        axios
        .get("http://localhost:4000/weather")
        .then(res => {
          this.datas = res.data;
        })
        .catch(err => console.log(err));
      }
    }
  }
};
</script>

<style>
</style>