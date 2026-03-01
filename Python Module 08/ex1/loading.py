try:
    import pandas
    import numpy
    import matplotlib.pyplot
    import requests
except ImportError as e:
    print(f"Error: Missing dependency - {e.name}")
    print("Please install the required libraries and try again.")
    print("pip install -r requirements.txt or \npoetry install")
    exit(1)

print("\nLOADING STATUS: Loading programs...\n")

print("Checking dependencies:")
print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
print(f"[OK] requests ({requests.__version__}) - Network requests ready")
print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
print("\nAnalyzing Matrix data...\nprocessing 1000 data points...")
data = numpy.random.rand(600, 6) * 100
print("Generating visualization...\n")
df = pandas.DataFrame(data, columns=['1', '2', '3', '4', '5', '6'])
means = df.mean()
means.plot(kind="bar")

matplotlib.pyplot.title('Matrix Data Analysis')
matplotlib.pyplot.savefig('matrix_analysis.png')
print("Analysis complete!")
print("Results saved to: matrix_analysis")
