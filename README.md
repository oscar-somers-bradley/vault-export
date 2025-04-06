# vault-export
<div id="top"></div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#usage">Limitations</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

### Installation


1. Clone the repo
   ```sh
git clone git@github.com:oscar-somers-bradley/vault-export.git
   ```
2. build docker image
   ```sh
   make build
   ```
3. Run the script
   ```sh
   docker run --rm hashicorp_vault_export:0.1
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

# `vault_export.py`
<!-- USAGE EXAMPLES -->
## Usage

This script has been created to export secrets from Hashicorp Vault instances with a version < 0.10.0. For versions > 0.10.0 (kv v1/v2), please use https://github.com/jonasvinther/medusa.
It will output to stdout a yaml file that can be then used by medusa to import the secrets into another vault instance please also use https://github.com/jonasvinther/medusa for the import.

Arguments:
 -  `-d` for the full path of the folder you want to get secrets from. example: https://example-vault0.test.com:8200/v1/foo/
 -  `-t` Vault token.
 -  `-l` This option is used to list all the secrets that will exported. This has a few limitations, please see below.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Limitations -->
## Limitations

- The app can only do one folder deep, so if you want all the secrets in https://example-vault0.test.com:8200/v1/foo/ but that folder contains a sub folder called bar/, it will not include it and you will need to run it again like this https://example-vault0.test.com:8200/v1/foo/bar/

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

 Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Oscar Somers-Bradley

Project Link: [https://github.com/oscar-bradley/vault-export-0.10.0]

<p align="right">(<a href="#top">back to top</a>)</p>
