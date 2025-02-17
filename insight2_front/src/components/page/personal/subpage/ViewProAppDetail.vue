<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-tickets"></i> 应用详情
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="container">
      <div class="block" id="vul_report">
        <el-form label-position="right"
		        :model="myproapp"
		        :ref="myproapp"
		        :rules="rules">

            <el-row >
                <el-form-item >
                  <span class="vuln-title insight_sensitive">项目: {{viewproapp.project_name}}-----应用:{{viewproapp.app_name}}</span>
                  <br />
                  <hr style="margin-top:2px;margin-bottom:2px;background-color:#606266;height: 1px;" />
                  <br />
                </el-form-item >
            </el-row>

			<el-row :gutter="20">
				<el-col :span="4">
					  <el-form-item label="测试内容" font-size=8pt></el-form-item>
				</el-col>
			</el-row>
			<el-row :gutter="10">
				<el-col :span="20" :offset="1">
					  <el-form-item label="">
						<span class="data-content insight_sensitive" type="text">{{viewproapp.content}} </span>
					  </el-form-item>
				</el-col>
			</el-row>
			<el-row :gutter="10">
				<el-col :span="4">
					  <el-form-item  label="资产入口地址:"> </el-form-item>
				</el-col>
			</el-row>
            <el-row :gutter="10">
				<el-col :span="20" :offset="1">
						<div style="width:50%;">
						  <div v-html="marked(filterXSS(viewproapp.asset_address)) " class="markdown-body insight_sensitive"></div>
						</div>
				</el-col>
			</el-row>
			<el-row :gutter="10">
				<el-col :span="4">
					  <el-form-item  label="用户口令信息"> </el-form-item>
				</el-col>
			</el-row>
			<el-row>
				<el-col :span="6" :offset="1">
						<el-form-item label="生产环境：" prop="produ_passwd">
							<el-input
							  placeholder="请输入本次项目密码"
							  v-model="myproapp.produ_passwd"
							  class="handle-input"
							  @keyup.enter.native="submitForm()"
							  show-password
							></el-input>
						</el-form-item>
                </el-col>
                <el-col :span="4">
                    <el-form-item >
                        <el-button type="primary" @click="submitForm">查看用户口令</el-button>
                    </el-form-item>
                </el-col>
			</el-row>
			<el-row :gutter="20">
				<el-col :span="8" :offset="1">
					<el-form-item label="口令：" prop="comment1">
						<el-input type="textarea"  resize="none" autosize placeholder="" v-model="myproapp.comment1"  readonly="true" v-show= "true"></el-input>
					</el-form-item>
				</el-col>
			</el-row>
            <el-row>
                <div class = "test-module">
                    <el-col :span="6" :offset="1">
                            <el-form-item label="测试环境：" prop="test_passwd">
                                <el-input
                                  placeholder="请输入本次项目密码"
                                  v-model="myproapp.test_passwd"
                                  class="handle-input"
                                  @keyup.enter.native="submitForm2()"
                                  show-password
                                ></el-input>
                            </el-form-item>
                    </el-col>
                    <el-col :span="4">
                        <el-form-item >
                            <el-button type="primary" @click="submitForm2">查看用户口令</el-button>
                        </el-form-item>
                    </el-col>
                </div>
			</el-row>
			<el-row :gutter="20">
				<el-col :span="8" :offset="1">
					<el-form-item label="口令：" prop="comment2">
						<el-input type="textarea"  resize="none" autosize placeholder="" v-model="myproapp.comment2"  readonly="true" v-show= "true"></el-input>
					</el-form-item>
				</el-col>
			</el-row>
			<el-row :gutter="20">
				<el-col :span="8" :offset="5">
				    <div class="final-confirm">
				        <el-button type="primary" @click="mark">标记本次应用测试完成</el-button>
				    </div>
				</el-col>
			</el-row>
		</el-form>
	  </div>
	</div>
  </div>
</template>

<script>
import Vue from "vue";
import Qs from "qs";
import {
  formatDate,
  trans_params,
  getStaticColors
} from "@/utils/common";
import { global_config } from "@/utils/global_config";

import  "static/css/markdown_style.css";
import html2Canvas from "html2canvas";
import JsPDF from "jspdf";
import Print from "print-js";

export default {
  data() {
    return {
      static_config: global_config,
      viewproapp: { self_rank: 0 },
      myproapp:{
        produ_passwd:"",
        comment1:"",
        test_passwd:"",
        comment2:""
      },
      rules: {
        produ_passwd: [
         { required: true, message: "请输入本次项目密码", trigger: "blur" }
        ],
        comment1: [
         { required: true, message: "请输入本次项目密码", trigger: "blur" }
        ],
        test_passwd: [
         { required: true, message: "请输入本次项目密码", trigger: "blur" }
        ],
         comment2: [
         { required: true, message: "请输入本次项目密码", trigger: "blur" }
        ]
      }
    };
  },
  computed: {
    risklevel: function() {
      if (this.viewvul.self_rank >= 0 && this.viewvul.self_rank < 6) {
        return "低危";
      } else if (this.viewvul.self_rank < 11) {
        return "中危";
      } else if (this.viewvul.self_rank < 16) {
        return "高危";
      } else if (this.viewvul.self_rank <= 20) {
        return "严重";
      } else {
        return "未知";
      }
    }
  },
  updated() {
    this.$desensitive();
  },
  created() {
    if (this.$route.query.app_id && this.$route.query.project_id) {
      console.log(this.$route.query.app_id);
      console.log(this.$route.query.project_id);
      this.$axios
        .get("/api/project/appget", { params: { project_id: this.$route.query.project_id,app_id: this.$route.query.app_id  } })
        .then(res => {
          console.log(res.data);
          this.viewproapp = res.data;
          if (res.data.status_code == 403) {
            this.$message.error("操作失败, " + res.data.msg);
          }
        });
    } else if (!this.$route.params.id) {
      this.$router.push("/n_my_projects");
    } else {
    }

    this.viewproapp = this.$route.params;
  },
  mounted() {
    this.$desensitive();
  },
  filters: {
    formatDate(time) {
      let date = new Date(Math.trunc(time * 1000));
      return formatDate(date, "yyyy-MM-dd HH:mm:ss");
    }
  },
  methods: {
	submitForm() {
		this.$axios
		  .post("/api/project/check_propwd", trans_params({ passwd: this.myproapp.produ_passwd,project_id:this.$route.query.project_id,app_id: this.$route.query.app_id}))
		  .then(res => {
		    if (res.data.status >= 1) {
		      this.$set(this.myproapp, "comment1", res.data.result)
		    } else
		      this.$message.error("密码错误请重试！");
		  });

	},
	submitForm2() {
		this.$axios
		  .post("/api/project/check_testpwd", trans_params({ passwd: this.myproapp.test_passwd,project_id:this.$route.query.project_id,app_id: this.$route.query.app_id }))
		  .then(res => {
		    if (res.data.status >= 1) {
		      this.$set(this.myproapp, "comment2", res.data.result)
		    } else
		      this.$message.error("密码错误请重试！");
		  });

	},
	mark(){
		this.$confirm("是否确认此操作", "提示", {
				confirmButtonText: "确认",
				cancelButtonText: "取消",
				type: "warning"
			})
			.then(() => {
				this.$axios
					.post("/api/project/app_mark", trans_params({
						project_id: this.$route.query.project_id,
						app_id: this.$route.query.app_id
					}))
					.then(res => {
						if (res.data.msg_status >= 1) {
							this.$message.success("状态已标记为完成");
						} else
							this.$message.error("标记失败, 已经是完成状态 ");
					});
			})
			.catch(() => {});
	},

  }
};
</script>



<style scoped>
.final-confirm {
  margin-top: 10px;
  margin-bottom: 20px;
}
.test-module {
  margin-top: 6px;
}

.handle-box {
  margin-bottom: 20px;
}

.handle-select {
  width: 120px;
}

.handle-input {
  width: 150px;

  display: inline-block;
}

.label {
  width: 90px;
  color: #99a9bf;
}
.el-form-item {
  font-size: 5px !important;
  margin-right: 0;
  margin-bottom: 0;
  margin-top: 5px;
  width: 90%;
}
.el-form-item--small.el-form-item {
  margin-bottom: 0 !important;
}
.data-content {
  color: rgb(71, 158, 216) !important;
  font-weight: bold;
}
.data-content-yellow {
  color: rgb(147, 153, 57) !important;
}
.data-content-orange {
  color: rgb(219, 39, 48) !important;
}
.data-content-grey {
  color: #69827c !important;
}
.data-content-blue {
  color: #112041;
}
.data-content-green {
  color: #20856d !important;
}
.vuln-title {
  font-size: 30px;
  font-weight: normal;
  line-height: 1.3;
  color: #20856d;
  letter-spacing: -1px;
  margin-bottom: 80px;
}

.block {
  border: solid 0.1px #dbdbdb;
  background: #f8f8f8;
  padding: 60px;
  margin: 10px;
}

</style>
