<script setup>
import { ref, watch } from "vue"
import { AMOUNT_RANGES } from "./constants.js"
import OrderTable from "./components/OrderTable.vue";
import Pagination from "./components/Pagination.vue"
import FilterBar from "./components/FilterBar.vue";

const orderList = ref([]);
const orderTotal = ref(0);
const currentPage = ref(1);
const statusFilter = ref(null);
const searchFilter = ref(null);
const dateFilter = ref(null);
const amountFilter = ref(null);
const sortBy = ref('created_at');
const sort = ref('descending');

const API_URL = import.meta.env.DEV
  ? 'http://localhost:8000'
  : 'https://fakeradmin.zeabur.app'

const fetchOrdersData = async () => {
  const params = new URLSearchParams();
  params.append('page', currentPage.value);
  params.append('sortBy', sortBy.value);
  params.append('sort', sort.value);

  if (statusFilter.value){
    params.append('status', statusFilter.value);
  }

  if (searchFilter.value){
    params.append('search', searchFilter.value);
  }

  if (dateFilter.value){
    params.append('date_start', dateFilter.value[0].toISOString());
    params.append('date_end', dateFilter.value[1].toISOString());
  }

  if (amountFilter.value){
    params.append('amount', AMOUNT_RANGES[amountFilter.value]);
  }

  const res = await fetch(
    `${API_URL}/order?${params}`
  );
  const data = await res.json();
  orderList.value = data.data;
  orderTotal.value = data.total;
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
