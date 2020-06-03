<template>
  <div>
    <h1 v-if="date == ''">Thời tiết ngày mai</h1>
    <h1 v-else>Thời tiết ngày {{ replaceDate }}</h1>
    <hr />
    <div class="card-deck">
      <CardWeather v-for="(data, i) in datas" v-bind:key="i" v-bind:data="data"></CardWeather>
    </div>
  </div>
</template>

<script>
import CardWeather from "./card/CardWeather";
import axios from "axios";
export default {
  data() {
    return {
      datas: [],
      date: ""
    };
  },
  components: {
    CardWeather
  },
  computed: {
    replaceDate(){
      return this.date.split('-').reverse().join('/');
    }
  },
  created() {
    if (this.$route.query.seach) {
      this.date = this.$route.query.seach;
      axios
        .get("http://localhost:4000/weather", {
          params: {
            seach: this.date
          }
        })
        .then(res => {
          this.datas = res.data;
          console.log(this.datas);
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
    $route(to, from){
      this.date = to.query.seach;
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
    }
  },
};
</script>

<style>
</style>