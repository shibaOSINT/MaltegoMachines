To use that machine, you'll need to add the linked .py file as a local transform. Please make sure the Transform ID is the following: "mathieugaucheler.aliasapttocisagovstring".




How to add the .py file as a local Transform:
https://docs.maltego.com/support/solutions/articles/15000017605-local-transforms-example

---

Alternatively, you can edit the machine, and **remove** the following line:
```
        run("mathieugaucheler.aliasapttocisagovstring")
```

You would then have to start your machine from a phrase (not an alias). Example of such phrase Entity: `"<APT NAME>" cisa.gov`