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
                <el-button
                    type="primary"
                    icon="el-icon-circle-plus"
                    @click="getAssetList();createVisible=true; form={enable:'1'}"
                    size="mini"
                >新增项目</el-button>
				<el-button
				    type="primary"
				    icon="el-icon-document-copy"
				    @click="copy()"
				    size="mini"
				>复制</el-button>
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
                <el-table-column prop="group_name" label="测试公司" min-width="150" sortable="custom">
                    <template slot-scope="scope">
                      <span>{{scope.row.group_name }}</span>
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
                        <span size="mini" v-tooltip="'编辑'" @click="cur_entity = scope.row;handleEdit(scope.$index, cur_entity)"
                        style="cursor:pointer !important">
                            <i class="el-iconbianji2 iconfont_no_margin sumeru_op_button"></i>
                        </span>
                        <span size="mini" v-tooltip="'删除'" type="danger" @click="dataDel(scope.row.id)">
                          <i class="el-iconshanchu1 iconfont_no_margin sumeru_op_button sumeru_red"></i>
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
        <!-- 新建 -->
        <el-dialog title="新建项目" :visible.sync="createVisible" width="50%">
          <el-form ref="createForm" :model="form" label-width="100px" :rules="rules">
            <el-form-item label="项目名称"  prop="project_name">
              <el-input v-model="form.project_name" clearable placeholder="项目名称" size="mini"></el-input>
            </el-form-item>

            <el-form-item label="测试公司" prop="group_name">
              <el-autocomplete
                v-model="form.group_name"
                :fetch-suggestions="querySearchAsyncGroup"
                placeholder="请输入内容"
                @select="handleSelectGroup"
              ></el-autocomplete>
            </el-form-item>
            <el-form-item label="项目密码"  prop="project_paw">
              <el-input v-model="form.project_paw"
                        clearable
                        placeholder="请输入项目密码"
                        show-password
                        size="mini"></el-input>
            </el-form-item>
            <el-form-item label="说明">
              <el-input type="textarea" :rows="2" placeholder="请输入内容" v-model="form.comment"></el-input>
            </el-form-item>
          </el-form>
          <span slot="footer" class="dialog-footer">
            <el-button type="primary" @click="doCreate()">创建</el-button>
          </span>
        </el-dialog>
        <!-- 编辑-->
        <el-dialog title="新建项目" :visible.sync="editVisible" width="50%">
          <el-form ref="createForm" :model="form" label-width="100px" :rules="rules">
            <el-form-item label="项目名称"  prop="project_name">
              <el-input v-model="form.project_name" clearable placeholder="项目名称" size="mini"></el-input>
            </el-form-item>

            <el-form-item label="测试公司" prop="group_name">
              <el-autocomplete
                v-model="form.group_name"
                :fetch-suggestions="querySearchAsyncGroup"
                placeholder="请输入内容"
                @select="handleSelectGroup"
              ></el-autocomplete>
            </el-form-item>
            <el-form-item label="项目密码"  prop="project_paw">
              <el-input v-model="form.project_paw"
                        clearable
                        placeholder="请输入项目密码"
                        show-password
                        size="mini"></el-input>
            </el-form-item>
            <el-form-item label="说明">
              <el-input type="textarea" :rows="2" placeholder="请输入内容" v-model="form.comment"></el-input>
            </el-form-item>
          </el-form>
          <span slot="footer" class="dialog-footer">
            <el-button type="primary" @click="doCreate()">修 改</el-button>
          </span>
        </el-dialog>
        </div>
    </template>

    <script>
        import Vue from "vue";
        import {
            getDateDiff_timestamp,
            formatDate,
            trans_params,
            getStaticColors_project,
            formatDatesecond
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
                    asset_list_url: "/api/asset/select",
                    role_list_url: "/api/role/select",
                    group_list_url: "/api/group/list",
                    add_url: "/api/project/add",
                    del_url: "/api/project/del",
					copy_url:"/api/project/copy",
                    createVisible: false,
                    editVisible:false,
                    tableData: [],
                    select_word: "",
                    cur_page: 1,
                    page_size: 10,
                    total: 0,
                    multipleSelection: [],
                    form: {
                        project_name: "",
                        group_name: "",
                        project_paw: ""
                    },
                    role_options: [{
                        value: "__",
                        label: "--"
                    }],
                    rules: {
                      project_name: [
                        { required: true, message: "请输入项目名称", trigger: "blur" }
                      ],
                      group_name: [
                        { required: true, message: "请选择渗透公司", trigger: "change" }
                      ],
                      project_paw: [
                        { required: true, message: "请输入项目密码", trigger: "blur" },
                      ],
                    },
                    static_config: global_config
                };
            },

            created() {
                this.getStatusGroup();
                this.getAssetList();
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
                getAssetList: function() {
                    this.$axios.get(this.asset_list_url + "?page_size=99999").then(res => {
                    this.asset_options = res.data.result;

                  });
                  this.$axios.get(this.asset_list_url + "?app_id=0&page_size=99999").then(res => {
                    this.asset_option_without_app = res.data.result;
                  });
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
                            path: "/project_app",
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
                doCreate(e) {
                  let cur_form = null;

                  if (this.$refs["createForm"]) {
                    cur_form = this.$refs["createForm"];
                  } else {
                    cur_form = this.$refs["editForm"];
                  }

                  cur_form.validate(valid => {
                    if (valid) {
                        this.$axios.post(this.add_url, trans_params(this.form)).then(res => {
                    if (res.data.status == 1) {
                      this.$message.success("操作成功");
                      this.getData();
                    } else
                    if(!res.data.status){
                      this.$message.error(
                        "操作失败, " +res.data.msg
                      );
                      }
                    this.createVisible = false;
                    this.editVisible = false;
                  });
                   }else {
                      this.$message.error("提交失败，请填写相应信息");
                    }
                  });
                },
                handleSelectionChange(val) {
                    this.multipleSelection = val;
                },
                filterProStatus(value, row, column) {
                  const property = column["property"];
                  return row[property].toString() === value;
                },
                dataDel(cur_del_node_id) {
                  // 数据删除，支持多个和单个删除

                  let to_del = null;

                  if (cur_del_node_id) {
                    to_del = cur_del_node_id;
                  } else {
                    if (this.multipleSelection.length <= 0) {
                      this.$message.info("未选择任何数据");
                      return;
                    }
                    this.del_list = this.multipleSelection.map(function(item) {
                      return item.id;
                    });
                    to_del = this.del_list;
                  }

                  this.$confirm("是否确认此操作", "提示", {
                    confirmButtonText: "确认",
                    cancelButtonText: "取消",
                    type: "warning"
                  })
                    .then(() => {
                      this.$axios
                        .post(this.del_url,  trans_params({ id: to_del }))
                        .then(res => {
                          if (res.data.status >= 1) {
                            this.getData();
                            this.$message.success("删除成功");
                          } else
                            this.$message.error("删除失败, 错误码: " + res.data.status);
                        });
                    })
                    .catch(() => {});
                },
				copy(cur_copy_node_id) {
				  // 数据复制，支持多个和单个删除

				  let to_copy = null;

				  if (cur_copy_node_id) {
				    to_copy = cur_copy_node_id;
				  } else {
				    if (this.multipleSelection.length <= 0) {
				      this.$message.info("未选择任何数据");
				      return;
				    }
				    this.copy_list = this.multipleSelection.map(function(item) {
				      return item.id;
				    });
				    to_copy = this.copy_list;
				  }
				  this.$confirm("是否确认此操作", "提示", {
				    confirmButtonText: "确认",
				    cancelButtonText: "取消",
				    type: "warning"
				  }).then(() => {
				      this.$axios
				        .post(this.copy_url,  trans_params({ id: to_copy }))
				        .then(res => {
				          if (res.data.status >= 1) {
				            this.getData();
				            this.$message.success("复制成功");
				          } else
				            this.$message.error("复制失败, 错误码: " + res.data.status);
				        });
				    })
				    .catch(() => {});
				},
                querySearchAsyncGroup(queryString, cb) {
                  this.$axios
                    .get(this.group_list_url, {
                      params: {
                        search: queryString,
                        page_size: 999
                      }
                    })
                    .then(res => {
                      let result = new Array();
                      res.data.result.map(function(v) {
                        result.push({ value: v.name, id: v.id, owner: v.owner });
                      });
                      cb(result);
                    });
                },
                handleSelectGroup(item) {
                  this.form.group_id = item.id;
                  //del by wuq
                 // if (item.owner) this.form.group_owner = item.owner;
                },
                handleEdit(index, row) {
                  this.editVisible = true;

                  this.form = row;

                  this.form.project_name = this.form.project_name.toString();
                  this.form.group_name =  this.form.group_name.toString();
                  this.form.project_paw = this.form.project_paw.toString();
                  this.form.comment = this.form.comment.toString();
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
