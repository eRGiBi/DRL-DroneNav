
def print_ppo_model_configuration(model):
    print("Training Configuration:")
    print("  Batch Size:", model.batch_size)
    print("  Number of Steps:", model.n_steps)
    print("  Clip Range:", model.clip_range)
    print("  Entropy Coefficient:", model.ent_coef)
    print("  Learning Rate:", model.learning_rate)
    print("  Gamma (discount factor):", model.gamma)
    print("  GAE Lambda:", model.gae_lambda)
    print("  Max Grad Norm:", model.max_grad_norm)
    print("  Number of Epochs:", model.n_epochs)
    print("  Target KL Divergence:", model.target_kl)
    print("  Use SDE (Stochastic Differential Equations):", model.use_sde)
    print("  SDE Sample Frequency:", model.sde_sample_freq)

    print("\nPolicy Configuration:")
    print("  Policy kwargs:", model.policy_kwargs)
    print("  Policy Class:", model.policy_class)

    print("\nOther Settings:")
    print("  Verbose:", model.verbose)
    print("  Tensorboard Log:", model.tensorboard_log)
    print("  Device:", model.device)
    print("  Vectorized Environment:", model._vec_normalize_env)


def print_sac_model_configuration(model):
    print("SAC Configuration:")
    print("  Batch Size:", model.batch_size)
    print("  Buffer Size:", model.buffer_size)
    print("  Learning Rate:", model.learning_rate)
    print("  Gamma (discount factor):", model.gamma)
    print("  Tau (soft update coefficient):", model.tau)
    print("  Entropy Coefficient:", model.ent_coef)
    print("  Target Entropy:", model.target_entropy)
    print("  Learning Rate Scheduler:", model.lr_schedule)
    print("  Number of Environments:", model.n_envs)
    print("  Number of Timesteps:", model.num_timesteps)

    print("\nPolicy Configuration:")
    print("  Policy kwargs:", model.policy_kwargs)
    print("  Policy Class:", model.policy_class)

    print("\nInternal State:")
    print("  Episode Number:", model._episode_num)
    print("  Last Observation:", model._last_obs)
    print("  Last Episode Starts:", model._last_episode_starts)
