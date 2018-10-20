def mxmul(mx1, mx2, nrow, nk, ncol):  # 矩阵乘法 （文件名mxmul是matrix multiplication简写）
    rst = [[0 for y in range(ncol)] for x in range(nrow)]
    for i in range(nrow):
        for j in range(ncol):
            for k in range(nk):
                rst[i][j] += mx1[i][k] * mx2[k][j]  # 进行矩阵乘法
    return rst  # 返回一个新矩阵


def mxsum(mx, nrow, ncol):  # 矩阵累加和
    s = 0
    for i in range(nrow):
        for j in range(ncol):
            s += mx[i][j]  # 进行矩阵元素求和
    return s


if __name__ == '__main__':  # Pycharm中直接敲main（Tab）即可 这是 测试代码部分
    import time

    nrow, nk, ncol = 50, 30, 50  # 调这里的值（下面2个注释分别运行哦）
    # nrow, nk, ncol = 100, 60, 100  # 调这里的值
    # nrow, nk, ncol = 500, 300, 500  # 调这里的值
    mx1 = [[y for y in range(nk)] for x in range(nrow)]
    mx2 = [[y for y in range(ncol)] for x in range(nk)]
    start = time.perf_counter()  # 计时start
    rst = mxmul(mx1, mx2, nrow, nk, ncol)  # 矩阵乘法
    end = time.perf_counter()  # 计时end
    print(f'运行时间为{end-start:.4f}s')  # 统计并输出运行时间
