<script setup>
import { ref } from "vue";

const data = ref([]);

const fetchData = async () => {
  const res = await fetch("https://fakeradmin.zeabur.app/");
  data.value = await res.json();
};

fetchData();
</script>

<template>
  <div v-for="i in data">{{ i }}</div>
  <el-button type="primary">I am ElButton</el-button>
</template>
