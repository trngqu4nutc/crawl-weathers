<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Trang chủ</a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <router-link tag="li" class="nav-item" to="/" active-class="active" exact>
          <a class="nav-link">Hôm nay</a>
        </router-link>
        <router-link tag="li" class="nav-item" v-bind:to="{path: '/weather'}" active-class="active">
          <a class="nav-link">Ngày mai</a>
        </router-link>
        <li class="nav-item dropdown">
          <a
            class="nav-link dropdown-toggle"
            href="#"
            id="navbarDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >Tùy chọn</a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link
              tag="a"
              v-bind:to="{ path: '/days', query: { number: 2 } }"
              class="dropdown-item"
            >2 ngày sau</router-link>
            <router-link
              tag="a"
              v-bind:to="{ path: '/days', query: { number: 3 } }"
              class="dropdown-item"
            >3 ngày sau</router-link>
            <router-link
              tag="a"
              v-bind:to="{ path: '/days', query: { number: 4 } }"
              class="dropdown-item"
            >4 ngày sau</router-link>
            <router-link
              tag="a"
              v-bind:to="{ path: '/days', query: { number: 5 } }"
              class="dropdown-item"
            >5 ngày sau</router-link>
            <router-link
              tag="a"
              v-bind:to="{ path: '/days', query: { number: 7 } }"
              class="dropdown-item"
            >7 ngày sau</router-link>
            <router-link
              tag="a"
              v-bind:to="{ path: '/days', query: { number: 10 } }"
              class="dropdown-item"
            >10 ngày sau</router-link>
            <router-link
              tag="a"
              v-bind:to="{ path: '/days', query: { number: 15 } }"
              class="dropdown-item"
            >15 ngày sau</router-link>
          </div>
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <input
          class="form-control mr-sm-2"
          type="date"
          placeholder="Search"
          v-model="date"
          aria-label="Search"
        />
      </form>
      <button class="btn btn-outline-success my-2 my-sm-0" v-on:click="show">Tìm kiếm</button>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      date: ""
    };
  },
  methods: {
    show() {
      if (this.date != "") {
        this.$router.push({
          path: "/weather",
          query: {
            seach: this.date
          }
        });
      }
    }
  }
};
</script>

<style>
</style>