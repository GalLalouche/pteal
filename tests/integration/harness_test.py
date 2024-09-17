import tempfile
import harness


def test_basic_harness_file():
  print_1: str = r"""
@.str = private unnamed_addr constant [3 x i8] c"%d\00", align 1

declare i32 @printf(i8*, ...)

define i32 @main() {
entry:
  %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i64 0, i64 0), i32 1)
  ret i32 0
}
  """
  with tempfile.NamedTemporaryFile(suffix=".ll") as temp_file:
    with open(temp_file.name, "w") as file:
      file.write(print_1)
      file.flush()
      result = harness.compile_and_run(temp_file.name)
      assert result == "1"
