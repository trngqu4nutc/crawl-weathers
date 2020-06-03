<template>
  <div>
    <h1 class="text-title">Cập nhật trong ngày</h1>
    <hr />
    <div class="card-deck">
      <Card v-for="(data, i) in datas" v-bind:key="i" v-bind:data="data"></Card>
    </div>
  </div>
</template>

<script>
import Card from "./card/Card";
import axios from 'axios';
export default {
  data() {
    return {
      datas: []
    };
  },
  components: {
    Card
  },
  created(){
      axios.get('http://localhost:4000/day')
        .then(res => {
            this.datas = res.data;
        })
        .catch(err => console.log(err));
      // setInterval(() => {
      //   this.datas = [];
      //   axios.get('http://localhost:4000/day')
      //   .then(res => {
      //       this.datas = res.data;
      //       console.log(res.data);
      //   })
      //   .catch(err => console.log(err));
      // }, 5000);
  }
};
</script>

<style>
</style>