def assert_task_exists_in_list(task_id, responseJson):
    assert any(t['id'] == task_id for t in responseJson['list']), f"La tarea con ID {task_id} no se encuentra en la lista de tareas"