<template>
  <table class="table table-hover" style="background-color: white; opacity: .8">
    <thead>
      <tr>
        <th scope="col">Thời gian</th>
        <th scope="col">Ảnh</th>
        <th scope="col">Trạng thái</th>
        <th scope="col">Nhiệt độ</th>
        <th scope="col">Cao nhất</th>
        <th scope="col">Thấp nhất</th>
      </tr>
    </thead>
    <tbody>
      <CardDetails v-for="(day, i) in days" v-bind:key="i" v-bind:day="day" />
    </tbody>
  </table>
</template>

<script>
import CardDetails from "./card/CardDetails";
import axios from "axios";
export default {
  props: ["date"],
  data() {
    return {
      days: []
    };
  },
  components: {
    CardDetails
  },
  created() {
    axios
      .get("http://localhost:4000/now", {
        params: {
          seach: this.date
        }
      })
      .then(res => {
        this.days = res.data;
      })
      .catch(err => console.log(err));
  },
  watch: {
    $route(to, from) {
      axios
        .get("http://localhost:4000/now", {
          params: {
            seach: this.date
          }
        })
        .then(res => {
          this.days = res.data;
        })
        .catch(err => console.log(err));
    }
  }
};
</script>

<style>
</style>