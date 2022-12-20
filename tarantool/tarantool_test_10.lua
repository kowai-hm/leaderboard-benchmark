-- Configure database
box.cfg {
   listen = 3301
}
-- Change admin password
box.schema.user.passwd('pass')
-- Init data
box.once("bootstrap", function()
	scores = box.schema.space.create('scores')
	scores:format({
		{name = 'user_id', type = 'unsigned'},
		{name = 'score', type = 'unsigned'}
	})
	scores:create_index('primary', {
		parts = {'user_id'}
	})
	scores:create_index('secondary', {
		unique = false,
		parts = {'score'}
	})
	-- Randomly generated data 
	scores:insert{1, 8}
	scores:insert{2, 20}
	scores:insert{3, 9}
	scores:insert{4, 13}
	scores:insert{5, 17}
	scores:insert{6, 18}
	scores:insert{7, 14}
	scores:insert{8, 11}
	scores:insert{9, 12}
	scores:insert{10, 17}
end)
