<script setup>
import { ref, watch } from "vue"
import OrderTable from "./components/OrderTable.vue";
import Pagination from "./components/Pagination.vue"
import FilterBar from "./components/FilterBar.vue";

const orderList = ref([]);
const orderTotal = ref(0);
const currentPage = ref(1);
const statusFilter = ref([]);
const inputFilter = ref();
const dateFilter = ref();
const amountFilter = ref();

const API_URL = import.meta.env.DEV
  ? 'http://localhost:8000'
  : 'https://fakeradmin.zeabur.app'

const fetchOrdersData = async () => {
  const res = await fetch(
    `${API_URL}/order?page=${currentPage.value}`
  );
  const data = await res.json();
  orderList.value = data.data;
  orderTotal.value = data.total;
};

watch(currentPage, () => {
  fetchOrdersData();
});

fetchOrdersData();

</script>

<template>
<h1>Order List</h1>
<FilterBar
  v-model:status-filter="statusFilter"
  v-model:input-filter="inputFilter"
  v-model:date-filter="dateFilter"
  v-model:amount-filter="amountFilter" />
<Pagination
  v-model:current-page="currentPage"
  :total=orderTotal />
<OrderTable
  :orders=orderList />
</template>
