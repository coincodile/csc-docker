CSC CLI
===================================================================

CoinEx is committed to product development and service improvement and contributes its 
share to the infrastructure of the blockchain world.
CSC is a small part of the development prospect. The CSC CLI is a basic tool to launch
relay node, validator and manage wallets.

This is a docker version of csc CLI.

Contribution is welcome.

## Usage

To show CSC CLI help:

.. code-blok:: bash
  
  docker run --interactive --rm \
     ghcr.io/coincodile/cetd \
         --help

## Initialize

to initialization, in terminal type:

.. code-blok:: bash

  docker run --interactive --rm \
    --volume .:/data \
    ghcr.io/coincodile/cetd \
      --datadir /data \
      init

This command will create the data directory and keystore directory under /path/your-data-localtion-fold, 
and create Genesis Block.If the default --datadir is not specified, it will create .cetd as the data 
directory and 'keystore' directory in the current user's home directory. As follows:


.. code-blok:: bash

       .
       ├── cetd
       │   ├── chaindata
       │   │   ├── 000001.log
       │   │   ├── CURRENT
       │   │   ├── LOCK
       │   │   ├── LOG
       │   │   └── MANIFEST-000000
       │   ├── lightchaindata
       │   │   ├── 000001.log
       │   │   ├── CURRENT
       │   │   ├── LOCK
       │   │   ├── LOG
       │   │   └── MANIFEST-000000
       │   ├── LOCK
       │   └── nodekey
       └── keystore

By default, init command is initialized to Mainnet information, and --testnet option is initialized to testnet information.

## Run

Startup command:

.. code-blok:: bash

  docker run --interactive --rm \
    --volume .:/data \
    ghcr.io/coincodile/cetd \
      --datadir /data

By default, the synchronization mode is fast, which can be changed to full mode with the option --syncmode full. We have
assigned P2P seed Node in cetd by default. You can change and assign trusted Seed Nodes via --bootnodes options.



