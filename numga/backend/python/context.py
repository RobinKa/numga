from numga.backend.python.operator import PythonSparseOperator
from numga.backend.python.multivector import PythonMultiVector
from numga.context import AbstractContext


class PythonContext(AbstractContext):
	def __init__(self, algebra, dtype=float):
		super(PythonContext, self).__init__(
			algebra=algebra,
			dtype=dtype,
			otype=PythonSparseOperator,
			mvtype=PythonMultiVector
		)
