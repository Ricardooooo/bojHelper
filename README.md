# 基于Elasticsearch的问答系统

### 环境配置
    
    Python版本为3.7
    ElasticSearch为6.4.2

### 启动方式
 注意：
    
    python app.py

### 目录说明
    
    data文件夹是结巴外部词典的数据
        dynasty.txt朝代
        extendWords.txt扩展词
        poem.txt诗词名
        poet.txt诗人名
        verse.txt诗句
        Poem.csv原始数据，直接导入ElasticSearch
    app.py
        main函数，在运行app.py之前，需要启动ElasticSearch服务
    elasticConnect.py
        ElasticSearch操作与数据解析
    loadData.py
        将诗词数据导入ElasticSearch
    questionAnalysis.py
        将自然语言转为对应的查询语句
    questionMapping.py
        问题映射
    wordHandle.py
        简单语言处理
    getReply.py
        查询ElasticSearch，获取回复文字