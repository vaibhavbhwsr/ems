-- Task CRUD

SELECT public.task_task_create(
        'Create CRUD for task',
        'Need APIs for Task create read update',
        40.0,
        '2024-01-25 09:00:00.507348+05:30',
        '2024-01-30 09:00:00.507348+05:30',
        1
    );
SELECT public.task_task_update(
        3,
        'Create CRUD for salary',
        'Need APIs for salary create read update',
        50.0,
        '2024-01-30 09:00:00.507348+05:30',
        '2024-02-05 09:00:00.507348+05:30',
        1
    )
SELECT public.task_task_list()
SELECT public.task_task_retrieve(2)
SELECT public.task_task_delete(3)

-- Attachment CRUD

SELECT public.task_attachment_create('img/default_dp.png', 2)
SELECT public.task_attachment_update(1, 'img/default_dp1.png', 2)
SELECT public.task_attachment_retrieve(1)
SELECT public.task_attachment_delete(2)

-- Employee CRUD

SELECT public.employee_employee_create(
	'Test5',
	'asdf@123',
	'Test5',
	'Five',
	'Test5@yopmail.com',
	'9898989895',
	'address',
	'Employee',
	'img/default.png',
	1,
	1
)

SELECT public.employee_employee_list()

-- DOCUMENT CRUD

SELECT public.employee_document_create(
	1,
	'file.pdf',
	'pan-card',
	FALSE
)