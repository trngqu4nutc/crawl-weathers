<template>
  <div>
    <h1 class="text-title" v-if="date == ''">Thời tiết ngày mai</h1>
    <div class="row" v-else>
      <div class="col-lg-10 col-md-10">
        <h1 class="text-title">Thời tiết ngày {{ replaceDate }}</h1>
      </div>
      <div class="col-lg-2 col-md-2">
        <button
          class="btn btn-outline-primary ml-12 float-right mt-3"
          style="color: #caf8ea;"
          v-on:click="changeComponents"
        >{{ btnText }}</button>
      </div>
    </div>
    <hr />
    <keep-alive>
      <component v-bind:is="currentTabComponent" v-bind:date="date"></component>
    </keep-alive>
  </div>
</template>

<script>
import DayDetails from "./DayDetails";
import TableDetails from "./TableDetails";
import axios from "axios";
export default {
  data() {
    return {
      date: "",
      currentTabComponent: "DayDetails",
      btnText: "Chi tiết"
    };
  },
  components: {
    DayDetails,
    TableDetails
  },
  methods: {
    changeComponents() {
      if (this.currentTabComponent == "DayDetails") {
        (this.currentTabComponent = "TableDetails"),
          (this.btnText = "Quay lại");
      } else {
        (this.currentTabComponent = "DayDetails"), (this.btnText = "Chi tiết");
      }
    }
  },
  computed: {
    replaceDate() {
      return this.date
        .split("-")
        .reverse()
        .join("/");
    }
  },
  watch: {
    $route(to, from) {
      this.date = to.query.seach;
    }
  },
  created() {
    if (this.$route.query.seach) {
      this.date = this.$route.query.seach;
    }
  }
};
</script>

<style>
</style>