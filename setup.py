import setuptools

setuptools.setup(name='ctffindPlot',
        version='0.0.1',
        description='Sequentially plot ctffind results from aligned micrographs',
        url='https://github.com/alberttxu/ctffindPlot',
        author='Albert Xu',
        author_email='albert.t.xu@gmail.com',
        license='MIT',
        packages=setuptools.find_packages(),
        install_requires=[
            'PyGnuplot',
            ],
        entry_points={
            'console_scripts': [
                'ctffindPlot = ctffindPlot.__main__:main'
                ]
            }
        )