def getUserInput(prompt):
  """
  Prompts the user for a non-empty input and returns the user's input.

  Args:
    prompt (str): The prompt to display to the user.

  Returns:
    str: The user's input.

  """
  while True:
    user_input = input(prompt)
    if not user_input:
      print("Please provide a valid input.")
    else:
      return user_input
