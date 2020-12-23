import questionAnalysis
import elasticConnect


def get_reply(question):
    es = elasticConnect.ElasticConnect()
    q2s = questionAnalysis.QuestionMatch(
        [u'./data/poem.txt', u'./data/poet.txt', u'./data/dynasty.txt', u'./data/verse.txt', u'./data/extendWords.txt'])

    num, values = q2s.get_resukt(question)
    reply = "没有找你要的答案，我会继续努力学习的喔"
    if values is not None:
        query = es.query_search(values)
        results = es.get_result(num, query)
        if len(results):
            if num < 10:
                reply = "、".join(results)
            else:
                words = results[0].split('，')
                poemLen = len(words)
                count = 0
                for word in words:
                    if word in question:
                        if ("下一句" in question) | ("下句" in question):
                            if count < (poemLen - 2):
                                reply = (words[count + 1])
                            else:
                                reply = "亲，已经到最后一句了喔"
                            break
                        if ("上一句" in question) | ("上句" in question):
                            if count == 0:
                                reply = "亲，这是第一句，没了上句啦"
                            else:
                                reply = words[count - 1]
                            break
                    count = count + 1
    return reply

