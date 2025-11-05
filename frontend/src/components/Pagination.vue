<script setup>
const props = defineProps(["total"]);
const currentPage = defineModel('currentPage')
</script>

<template>
  <el-row justify="center">
    <el-pagination
      v-model:current-page="currentPage"
      :total="total"
      layout="prev, pager, next" />
  </el-row>
</template>
