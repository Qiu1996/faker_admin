<script setup>
import { ref, watch } from "vue"
import { AMOUNT_RANGES } from "./constants.js"
import OrderTable from "./components/OrderTable.vue";
import Pagination from "./components/Pagination.vue"
import FilterBar from "./components/FilterBar.vue";

const orderList = ref([]);
const orderTotal = ref(0);
const currentPage = ref(1);
const statusFilter = ref([]);
const searchFilter = ref('');
const dateFilter = ref();
const amountFilter = ref();
const sortBy = ref('created_at');
const sort = ref('descending');

const API_URL = import.meta.env.DEV
  ? 'http://localhost:8000'
  : 'https://fakeradmin.zeabur.app'

const fetchOrdersData = async () => {
  const page = `page=${currentPage.value}`;
  const sort_para = `sortBy=${sortBy.value}&sort=${sort.value}`;
  const date_format = dateFilter.value ? `${dateFilter.value[0].toISOString()},${dateFilter.value[1].toISOString()}` : '';
  const amount = amountFilter.value ? `${AMOUNT_RANGES[amountFilter.value]}` : '';
  const filter_para = `status=${statusFilter.value}&search=${searchFilter.value}&date=${date_format}&amount=${amount}`;

  const res = await fetch(
    `${API_URL}/order?${page}&${sort_para}&${filter_para}`
  );
  const data = await res.json();
  orderList.value = data.data;
  orderTotal.value = data.total;

  console.log(`${API_URL}/order?${page}&${sort_para}&${filter_para}`);

};

watch(
  [currentPage, statusFilter, searchFilter, dateFilter, amountFilter], () => {
    fetchOrdersData();
  }
)

fetchOrdersData();

const handleSort = async ({prop, order}) => {
  sortBy.value = prop;
  sort.value = order;
  fetchOrdersData();
}

</script>

<template>
<h1>Order List</h1>
<FilterBar
  v-model:status-filter="statusFilter"
  v-model:search-filter="searchFilter"
  v-model:date-filter="dateFilter"
  v-model:amount-filter="amountFilter" />
<Pagination
  v-model:current-page="currentPage"
  :total=orderTotal />
<OrderTable
  @sort-change="handleSort"
  :orders=orderList />
</template>
