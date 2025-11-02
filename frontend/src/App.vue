<script setup>
import { ref, computed } from "vue"
import OrderTable from "./components/OrderTable.vue";
import Pagination from "./components/Pagination.vue"

const orders = ref([]);
const currentPage = ref(1);
const pageSize = ref(10);

const fetchOrdersData = async () => {
  const res = await fetch("https://fakeradmin.zeabur.app/");
  orders.value = await res.json();
};
fetchOrdersData();

const displayedOrders = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  const end = start + pageSize.value
  return orders.value.slice(start, end)
})

</script>

<template>
<h1>Order List</h1>
<Pagination
  v-model:current-page="currentPage"
  :page-size=pageSize
  :total=orders.length />
<OrderTable :orders=displayedOrders />
</template>
