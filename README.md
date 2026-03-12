# 人工智能导论课程作业 02

## 目录结构

hw02/
- README.md                    # 本文件
- 导读_LLaMA_Open_and_Efficient_Foundation_Language_Models.md  # 论文导读文档
- chatbot_deepseek.py          # Chatbot 示例代码
- requirements.txt             # 依赖项

## 任务一：论文导读

### 论文信息
- 论文标题：LLaMA: Open and Efficient Foundation Language Models
- 作者：Meta AI Research团队
- 出处：Meta AI Research
- 年份：2023
- 使用的大模型：DeepSeek

### 论文导读内容
- 论文概览：介绍LLaMA系列模型的基本信息和主要贡献
- 核心方法：详细描述模型架构、训练数据和训练策略
- 实验结果：分析在基准测试上的表现和下游任务适应能力
- 技术创新：探讨数据处理优化和训练效率提升的方法
- 影响与意义：评估LLaMA对开源社区和技术发展的贡献
- 局限性与未来方向：讨论模型的不足和未来改进的可能性
- 总结：对LLaMA系列模型的整体评价和意义

## 任务二：Chatbot 示例代码

### 采用的 API/平台
- API 类型：DeepSeek API
- 平台：DeepSeek 官方 API

### 功能说明
- 基于DeepSeek API实现的简单聊天机器人
- 支持实时对话交互
- 包含错误处理机制
- 支持通过环境变量或直接修改代码配置API Key

### 运行方式
1. 安装依赖：pip install -r requirements.txt
2. 配置 API Key：
   - 方法 1：设置环境变量 DEEPSEEK_API_KEY
   - 方法 2：直接在代码中修改 API_KEY 变量
3. 运行命令：python chatbot_deepseek.py
4. 交互方式：输入消息后按回车，输入exit退出

### 代码结构
- chat_with_deepseek()：核心函数，负责调用DeepSeek API获取回复
- 主函数：处理用户输入和输出，实现交互循环