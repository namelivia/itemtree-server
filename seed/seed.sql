--Insert some test items
INSERT INTO items (id, name, description, parent_id, destination_id, is_container) VALUES (1, 'Test item 1', 'This is test item 1', NULL, 1, FALSE);
INSERT INTO items (id, name, description, parent_id, destination_id, is_container) VALUES (2, 'Test item 2', 'This is test item 2', 1, 1, FALSE);
INSERT INTO items (id, name, description, parent_id, destination_id, is_container) VALUES (3, 'Test item 3', 'This is test item 3', 1, 1, FALSE);
INSERT INTO items (id, name, description, parent_id, destination_id, is_container) VALUES (4, 'Test item 4', 'This is test item 4', 3, 1, FALSE);
INSERT INTO items (id, name, description, parent_id, destination_id, is_container) VALUES (5, 'Test item 5', 'This is test item 5', NULL, 1, FALSE);
INSERT INTO comments (id, content, item_id, user_id, user_name) VALUES (1, 'Test comment 1', 1, 'localhost/testuser', 'Test User');
INSERT INTO comments (id, content, item_id, user_id, user_name) VALUES (2, 'Test comment 2', 1, 'localhost/testuser', 'Test User');
