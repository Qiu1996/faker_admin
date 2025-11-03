<script setup>
import { ref, computed } from "vue"
import OrderTable from "./components/OrderTable.vue";
import Pagination from "./components/Pagination.vue"
import FilterBar from "./components/FilterBar.vue";

const orderList = ref([]);
const currentPage = ref(1);
const pageSize = ref(10);
const statusFilter = ref([]);

const API_URL = import.meta.env.DEV
  ? 'http://localhost:8000'
  : 'https://fakeradmin.zeabur.app'

const fetchOrdersData = async () => {
  const res = await fetch(`${API_URL}/`);
  orderList.value = await res.json();
};
fetchOrdersData();

const filteredOrders = computed(() => {
  let result = orderList.value

  if (statusFilter.value.length > 0) {
    result = result.filter(order =>
      statusFilter.value.includes(order.status)
    )
  }

  return result
})


const displayedOrders = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  const end = start + pageSize.value
  return filteredOrders.value.slice(start, end)
})

const handleSort = ({ prop, order }) => {
  if (!order) {
    orderList.value.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    return;
  }

  const direction = order === "ascending" ? -1 : 1;

  const comparators = {
    order_number: (item1, item2) => item1.localeCompare(item2),
    customer_name: (item1, item2) => item1.localeCompare(item2, "zh-TW"),
    amount: (item1, item2) => item1 - item2,
    status: (item1, item2) => item1.localeCompare(item2),
    created_at: (item1, item2) => new Date(item1) - new Date(item2)
  };

  orderList.value.sort((item1, item2) =>
    comparators[prop](item1[prop], item2[prop]) * direction
  );
}

</script>

<template>
<h1>Order List</h1>
<FilterBar
  v-model:statusFilter="statusFilter" />
<Pagination
  v-model:current-page="currentPage"
  :page-size=pageSize
  :total=filteredOrders.length />
<OrderTable
  :orders=displayedOrders
  @sort-change="handleSort"
  />
</template>
