from multiprocessing import Process
import os


# 子进程要执行的代码
def run_pro(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # Process 创建一个进程实例
    p = Process(target=run_pro, args=('test',))
    print('Child process will start.')
    # 启动子进程
    p.start()
    # 等待子进程结束后再继续往下运行
    p.join()
    print('Child process end.')


