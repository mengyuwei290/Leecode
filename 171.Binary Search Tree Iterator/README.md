其实就是中序遍历, 一直保持stack的最后node是当前的最小值, hasMin其实就是len(stack) > 0, 每次pop出最小值后, 将该node的right进行中序遍历.
