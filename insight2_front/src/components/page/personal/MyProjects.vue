<template>
	<div>
		<div class="crumbs">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item>
					<i class="el-icon-tickets"></i> 项目
				</el-breadcrumb-item>
				<el-breadcrumb-item>我的项目</el-breadcrumb-item>
			</el-breadcrumb>
		</div>

		<div class="container">
			<div class="handle-box">
				<el-input size="mini" v-model="select_word" placeholder="请输入关键词" class="handle-input"
					@keyup.enter.native="search()"></el-input>
				<el-select size="mini" v-model="select_project_status" placeholder="状态筛选" class="handle-select mr10">
					<el-option v-for="item in status_options" :key="item.id" :label="item.name" :value="item.id">
						<span style="float: left">{{ item.name }}</span>
						<span style="float: right; color: #8492a6; font-size: 13px">{{ item.count }}</span>
					</el-option>
				</el-select>
				<el-button type="primary" icon="el-icon-search" @click="search" size="mini">搜索</el-button>
			</div>

			<!-- 表头操作 -->
			<el-table :data="tableData" border @selection-change="handleSelectionChange"
				@current-change="handleCurrentChangeRow" highlight-current-row @sort-change="sortChange">

				<el-table-column type="selection" width="45"></el-table-column>
				<!-- add by wuq -->
				<el-table-column prop="project_date" label="日期" min-width="100" sortable="custom">
					<template slot-scope="scope">
                        <el-tooltip
                          effect="light"
                          :content="scope.row.project_date | formatDatesecond"
                          placement="right"
                        >
					        <span class="project_date_tag">{{scope.row.project_date | formatDate }}</span>
					    </el-tooltip>
					</template>
				</el-table-column>
				<el-table-column prop="project_name" label="项目名称" min-width="150" sortable="custom">
					<template slot-scope="scope">
					  <span
					    class="primary-title insight_sensitive"
					    @click="cur_entity = scope.row;viewProject()"
					    style="cursor:pointer !important"
					  >{{scope.row.project_name }}</span>
					</template>
				</el-table-column>
				<el-table-column prop="project_status" label="状态" min-width="70"
					:filters="[{ text: '已完成', value: '1' }, { text: '未完成', value: '0' }]"
					:filter-method="filterProStatus" filter-placement="bottom-end">
					<template slot-scope="scope">
					  <span class="in-tag">{{ scope.row.project_status}}</span>
					</template>
					<template slot-scope="scope">
					  <span  class="in-tag"
					    :style="{'color':statusColor_project(scope.row.project_status) }"
					  >{{scope.row.project_status | statusNameFilter("PROJECT_STATUS","未处理")}}</span>
					</template>
				</el-table-column>

				<!--add by wuq-->
				<el-table-column label="操作" min-width="100">
					<template slot-scope="scope">
						<span size="mini" v-tooltip="'查看'" @click="cur_entity = scope.row;viewProject()"
						style="cursor:pointer !important">
							<i class="el-iconbianji2 iconfont_no_margin sumeru_op_button"></i>
						</span>
					</template>
				</el-table-column>

			</el-table>

			<!--分页代码-->
			<div class="pagination">
				<el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange"
					:current-page.sync="cur_page" :page-sizes="[10, 20, 50,100]" :page-size.sync="page_size"
					layout="total, sizes, prev, pager, next, jumper" :total.sync="total"></el-pagination>
			</div>
		</div>
	</div>
</template>

<script>
	import Vue from "vue";
	import {
		getDateDiff_timestamp,
		formatDate,
		formatDatesecond,
		trans_params,
		getStaticColors_project,
	} from "@/utils/common";
	import {
		global_config
	} from "@/utils/global_config";
	import bus from "@/components/common/bus";

	export default {
		name: "curd",
		components: {},
		data() {
			let that = this;
			var checkAppID = (rule, value, callback) => {
				that.$nextTick(() => {
					console.log(this.form.app_id);
				});
				if (!value) {
					return callback(new Error("请选择关联应用!!!"));
				} else {
					return true;
				}
			};

			return {
				select_project_status: null,
				app_id: null,
				app_id_name: null,
				status_options: [{
					value: "0",
					label: "未审核"
				}],
				cur_entity: {},
				list_url: "/api/project/my/list",
				role_list_url: "/api/role/select",
				tableData: [],
				select_word: "",
				cur_page: 1,
				page_size: 10,
				total: 0,
				multipleSelection: [],
				form: {
					self_rank: "1",
					layer: 10,
					app_id: -1
				},
				role_options: [{
					value: "__",
					label: "--"
				}],
				static_config: global_config
			};
		},

		created() {
			this.getStatusGroup();
			this.getRoleList();
			this.getData();
		},
		updated() {
			this.$desensitive();
		},
		computed: {
			colortype: function() {
				if (this.form.self_rank >= 0 && this.form.self_rank < 6) {
					return "success";
				} else if (this.form.self_rank < 11) {
					return "";
				} else if (this.form.self_rank < 16) {
					return "danger";
				} else if (this.form.self_rank <= 20) {
					return "warning";
				}
			},

		},

		filters: {
			getDateDiff_timestamp(time) {
				return getDateDiff_timestamp(time);
			},
			formatDate(time) {
				let date = new Date(Math.trunc(time * 1000));
				return formatDate(date, "yyyy-MM-dd ");
			},
            formatDatesecond(time) {
			  let date = new Date(Math.trunc(time * 1000));
			  return formatDatesecond(date, "yyyy-MM-dd HH:mm:ss");
			},
			statusFilter(status) {
				const statusMap = {
					"0": "info",
					"1": "success",
					"-1": "danger"
				};
				return statusMap[status];
			},
			statusNameFilter(status, name, default_status = "其他") {
				// filt ers:{ filter:function(data,arg1,arg2){ return ... } }
				let statusName = global_config[name][status];
				if (global_config[name][status]) {
					return global_config[name][status];
				} else {
					return default_status;
				}
			}
		},

		methods: {
			statusColor_project(status) {
				return getStaticColors_project(status);
			},

			handleSelect(item) {
				this.form.app_id = item.id;
				this.form.app_name = item.value;
			},
			handleSelectPaper(item) {
				this.form.article_id = item.id;
				this.form.solution_name = item.value;
			},
			getRoleList: function() {
				this.$axios
					.get(this.role_list_url, {
						params: {
							type: 0
						}
					})
					.then(res => {
						this.role_options = res.data.result;
						console.log(this.role_options);
					});
			},
			sortChange: function(column, prop, order) {
				this.sortcolumn = column.prop;
				this.sortorder = column.order;
				this.getData();
			},

			viewProject() {
				console.log(this.cur_entity);
				if (this.cur_entity.id) {
					let routes = this.$router.resolve({
						name: "n_viewprojectdetail",
						query: {
							id: this.cur_entity.id
						}
					});

					window.open(routes.href, "_blank");
				} else {
					this.$message.info("请选择数据");
				}
			},

			getStatusGroup() {
				this.$axios.get("api/project/my/status/group").then(res => {
					this.status_options = res.data.result;
				});
			},
			getData() {
				this.$axios
					.get(this.list_url, {
						params: {
							search: this.select_word,
							page_index: this.cur_page,
							page_size: this.page_size,
							sort: this.sortcolumn,
							direction: this.sortorder,
							project_status: this.select_project_status
						}
					})
					.then(res => {
						this.tableData = res.data.result;
						this.total = res.data.total;
					});
			},

			handleSizeChange(val) {
				this.page_size = val;
				this.getData();
			},

			handleCurrentChange(val) {
				this.cur_page = val;
				this.getData();
			},
			handleCurrentChangeRow(val) {
				this.cur_entity = val;
			},

			search() {
				this.getData();
			},

			handleSelectionChange(val) {
				this.multipleSelection = val;
			},
			filterProStatus(value, row, column) {
			  const property = column["property"];
			  return row[property].toString() === value;
			}
		}
	};
</script>

<style scoped>
	.handle-box {
		margin-bottom: 20px;
	}

	.handle-select {
		width: 120px;
	}

	.handle-input {
		width: 200px;
		display: inline-block;
	}
</style>
